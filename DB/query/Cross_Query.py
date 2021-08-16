
# curl --location --request GET 'http://172.17.254.187:8880/dmesg.log' \
# --header 'Content-Type: application/json' \
# --data '{"raw_message": "B81019Z1000572800008J0SA | B81.019Z1.0005 | SV300G3 | [388150.357236] cool docker: kernal panic error"}'


# curl --location --request GET 'http://172.17.254.187:9880/sel.log' \
# --header 'Content-Type: application/json' \
# --data '{"raw_message": "B81019Z1000572800008J0SA | B81.019Z1.0005 | SV300G3 | e | 11/21/2018 | 23:43:20 | Kernel CPU0_ERR | so panic | Asserted"}'

Cross_log_error = {
    "track_total_hits": true,
    "query": {
        "bool": {
            "should": [
                {
                "match": {
                    "status": {
                        "query": "asserted",
                        "boost": 10
                    }
                }
            },
            ]
        }
    },
    "size": 100
}