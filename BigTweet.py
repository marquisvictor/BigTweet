 #!/usr/bin/env python3

import os
import sys
import re
import getopt
import traceback

if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

import BigTweet as bt

def main(argv):
    if len(argv) == 0:
        print('You must pass some parameters')
        return

    if len(argv) == 1:
        print(__doc__)
        return

    try:
        opts, args = getopt.getopt(argv, "", ("querysearch=",
                                              "since=",
                                              "until=",
                                              "near=",
                                              "within=",
                                              "toptweets",
                                              "maxtweets=",
                                              "lang=",
                                              "output=",
                                              "debug"))

        tweetCriteria = bt.manager.TweetCriteria()
        outputFileName = "output_got.csv"

        debug = False
        
        for opt, arg in opts:
            if opt == '--querysearch':
                tweetCriteria.querySearch = arg


            elif opt == '--since':
                tweetCriteria.since = arg

            elif opt == '--until':
                tweetCriteria.until = arg

            elif opt == '--near':
                geocode = arg.split(',')
                try:
                    if len(geocode) != 2:
                        raise
                    lat, lon = geocode[0].strip(), geocode[1].strip()
                    if lat[-1].lower() == 'n':
                        lat = float(lat[:-1])
                    elif lat[-1].lower() == 's':
                        lat = -float(lat[:-1])
                    else:
                        lat = float(lat)

                    if lon[-1].lower() == 'e':
                        lon = float(lon[:-1])
                    elif lon[-1].lower() == 'w':
                        lon = -float(lon[:-1])
                    else:
                        lon = float(lon)
                    if lat < -180 or lat > 180:
                        raise
                    if lon < -90 or lon > 90:
                        raise
                    tweetCriteria.lat = lat
                    tweetCriteria.lon = lon
                except:
                    tweetCriteria.near = arg

            elif opt == '--within':
                tweetCriteria.within = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = True

            elif opt == '--maxtweets':
                tweetCriteria.maxTweets = int(arg)

            elif opt == '--lang':
                tweetCriteria.lang = arg

            elif opt == '--output':
                outputFileName = arg

            elif opt == '--debug':
                debug = True

        if debug:
            print(' '.join(sys.argv))
            print("BigTweet", bt.__version__)    

        

        outputFile = open(outputFileName, "w+", encoding="utf8")
        outputFile.write('date,username,to,replies,retweets,favorites,text,geo,mentions,hashtags,id,permalink\n')

        cnt = 0
        def receiveBuffer(tweets):
            nonlocal cnt

            for t in tweets:
                data = [t.date.strftime("%Y-%m-%d %H:%M:%S"),
                    t.username,
                    t.to or '',
                    t.replies,
                    t.retweets,
                    t.favorites,
                    '"'+t.text.replace('"','""')+'"',
                    t.geo,
                    t.mentions,
                    t.hashtags,
                    t.id,
                    t.permalink]
                data[:] = [i if isinstance(i, str) else str(i) for i in data]
                outputFile.write(','.join(data) + '\n')

            outputFile.flush()
            cnt += len(tweets)

            if sys.stdout.isatty():
                print("\rSaved %i"%cnt, end='', flush=True)
            else:
                print(cnt, end=' ', flush=True)

        print("Downloading tweets...")
        bt.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer, debug=debug)

    except getopt.GetoptError as err:
        print('Arguments parser error')
        print('\t' + str(err))

    except KeyboardInterrupt:
        print("\r\nInterrupted.\r\n")

    except Exception as err:
        print(traceback.format_exc())
        print(str(err))

    finally:
        if "outputFile" in locals():
            outputFile.close()
            print()
            print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
    main(sys.argv[1:])
