from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://brice:bYUwmeLyq8yEW@cluster0.rdty5gv.mongodb.net/')
result = client['sample_analytics']['transactions'].aggregate([
    {
        '$match': {
            '$and': [
                {
                    'transaction_count': {
                        '$gte': 80
                    }
                }, {
                    'transaction_count': {
                        '$lte': 100
                    }
                }, {
                    'transactions.symbol': 'goog'
                }
            ]
        }
    }, {
        '$lookup': {
            'from': 'accounts',
            'localField': 'account_id',
            'foreignField': 'account_id',
            'as': 'products_infos'
        }
    }, {
        '$lookup': {
            'from': 'customers',
            'let': {
                'account_id': '$account_id'
            },
            'pipeline': [
                {
                    '$match': {
                        '$expr': {
                            '$in': [
                                '$$account_id', '$accounts'
                            ]
                        }
                    }
                }
            ],
            'as': 'user_info'
        }
    }, {
        '$replaceRoot': {
            'newRoot': {
                '$mergeObjects': [
                    {
                        '$arrayElemAt': [
                            '$user_info', 0
                        ]
                    }, '$$ROOT'
                ]
            }
        }
    }, {
        '$project': {
            'transactions': 1,
            'account_id': 1,
            'products': 1,
            'name': 1,
            'email': 1,
            'products_infos.products': 1
        }
    }
])