# bili_video_partition_spyder
## 简介
一个爬取b站分区视频信息的爬虫（伪）
## 功能
- [] 爬取B站各分区视频总量和热门视频数据
- [] 根据数据形成图表

## 使用的API及说明
1.https://api.bilibili.com/x/web-interface/ranking/region?day=7&rid=157

爬取分区热门视频的信息，rid为分区对应tid号，见[分区代码](https://socialsisteryi.github.io/bilibili-API-collect/docs/video/video_zone.html#%E5%8A%A8%E7%94%BB)

2.https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&copy_right=-1&new_web_tag=1&order=click&cate_id=182&page=1&pagesize=30&time_from=(开始日期)&time_to=(现在日期)

爬取分区数据，其中包含分区视频数量，cate_id为分区对应tid号


目前B站有21个有效大分区，各大分区下有众多小分区，小分区共计有