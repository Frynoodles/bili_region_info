# bili_video_partition_spyder
## 简介
一个爬取b站分区视频信息的爬虫（伪）
## 采集的数据
- 每个分区的热门视频前十，并会对他们的观看、硬币数、收藏量汇总统计
- 每个分区最近7天的视频数量


## 数据介绍
- 生成的数据在[output](./output/)文件夹下
- 分区的id等信息在文件[region_data.json](./resources/region_data.json)中
- ------
- tid 分区代码，也是rid
- 名称 分区的名称
- 代号 分区的代号
- 简介 对分区的介绍
- url路由 对应的b站url中的路由/地址
- 主分区 该分区所属的主分区
- hot_data 当前热门视频数据（未处理
- hot_video_total_play 统计的热门数据的播放量之和
- hot_video_total_coins 统计的热门数据的硬币之和
- hot_video_total_favorites 统计的热门视频的收藏之和
- hot_video_nums_7 最近7天内该区的投稿数量


## 使用的API及说明
1.https://api.bilibili.com/x/web-interface/ranking/region?day=7&rid=157

爬取分区热门视频的信息，rid为分区对应tid号，见[分区代码](https://socialsisteryi.github.io/bilibili-API-collect/docs/video/video_zone.html#%E5%8A%A8%E7%94%BB)

2.https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1&new_web_tag=1&order=click&cate_id=182&page=1&pagesize=30&time_from=(开始日期)&time_to=(现在日期)

爬取分区数据，其中包含分区视频数量，cate_id为分区对应tid号



## 目前B站有21个有效大分区，各大分区下有众多小分区，小分区共计有115个（2023年3月27日）


## 本库使用到了[bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)的部分API信息和分区统计，感谢大佬