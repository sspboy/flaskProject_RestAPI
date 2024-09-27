# 数字人

# 选择数字人合成【文字合成、音频文件合成、音频文件地址合成】

# 定制数字人：专业版、大众版


# 文字合成

task = {
    "VideoTracks": [{
        "VideoTrackClips": [{
            "Type": "GlobalImage",
            "MediaId": "7980d8f************e6f7e5696301"
        }]
    }, {
        "VideoTrackClips": [{
            "Comment": "数字人-输入为文字",
            "Type": "AI_Avatar",
            "AvatarId": "fanyu-broadcast_standing",
            "Content": "近日，随着消费升级和物流技术的发展，仓储式购物逐渐受到消费者的欢迎。据了解，这种购物方式是指将商品储存在仓库中，顾客通过线上平台选择商品后，到物流中心自行提取商品。避免了传统购物的排队、拥堵等问题，同时也提高了商品的物流效率和安全性。目前，不少电商企业已经开始尝试仓储式购物，成为未来新零售的重要趋势之一。",
            "Voice": "zhitian",
            "Effects": [{
                "Type": "AI_ASR",
                "Font": "Alibaba PuHuiTi",
                "FontSize": 60,
                "Spacing": 1,
                "Ratio": 1
            }]
        }]
    }]
}

# 音频文件MediaId合成
task2 = {
    "VideoTracks": [{
        "VideoTrackClips": [{
            "Type": "GlobalImage",
            "MediaId": "eb2dd180********92ee7e7d75b6301"
        }]
    }, {
        "VideoTrackClips": [{
            "Comment": "数字人-输入为音频 MediaId",
            "Type": "AI_Avatar",
            "AvatarId": "fanyu-broadcast_standing",
            "MediaId": "596cbd10e********b6e6f7e5696302",
            "Effects": [{
                "Type": "AI_ASR",
                "Font": "Alibaba PuHuiTi",
                "FontSize": 60,
                "Spacing": 1,
                "Ratio": 1
            }]
        }]
    }]
}

# 音频文件地址合成
task3 = {
    "VideoTracks": [{
        "VideoTrackClips": [{
            "Type": "GlobalImage",
            "MediaId": "7980d8f************e6f7e5696301"
        }]
    }, {
        "VideoTrackClips": [{
            "Comment": "数字人-输入为音频 MediaURL",
            "Type": "AI_Avatar",
            "AvatarId": "fanyu-broadcast_standing",
            "MediaURL": "https://your_bucket.oss-cn-shanghai.aliyuncs.com/your_audio.mp3",
            "Effects": [{
                "Type": "AI_ASR",
                "Font": "Alibaba PuHuiTi",
                "FontSize": 60,
                "Spacing": 1,
                "Ratio": 1
            }]
        }]
    }]
}