#!/usr/bin/python3
"""reads stdin line by line and computes metrics """
import sys


if __name__ == '__main__':

    def printResults(statusCodes, fileSize):
        """Print statistics """
        print("File size: {:d}".format(fileSize))
        for statusCode, times in sorted(statusCodes.items()):
            if times:
                print("{:s}: {:d}".format(statusCode, times))

    statusCodes = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0
                   }
    fileSize = 0
    nLines = 0

    try:
        """ Read stdin line by line """
        for line in sys.stdin:
            if nLines != 0 and nLines % 10 == 0:
                """ After every 10 lines, print from the beginning """
                printResults(statusCodes, fileSize)
            nLines += 1
            data = line.split()
            try:
                """ Compute metrics """
                statusCode = data[-2]
                if statusCode in statusCodes:
                    statusCodes[statusCode] += 1
                fileSize += int(data[-1])
            except Exception:
                pass
        printResults(statusCodes, fileSize)
    except KeyboardInterrupt:
        """ Keyboard interruption, print from the beginning """
        printResults(statusCodes, fileSize)
        raise
