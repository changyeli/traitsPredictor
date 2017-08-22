library(rga)
library(lubridate)
library(ggplot2)
library(readr)
id = 88531234

blog = read_delim("~/Documents/scripts/blog.txt", 
                   "\n", escape_double = FALSE, col_names = FALSE, 
                   trim_ws = TRUE)
colnames(blog) = "pageTitle"
dt1 = ga$getData(id, start.date = "2016-09-01", end.date = "2017-07-27",
                 batch = TRUE, walk = TRUE,
                 metrics = "ga:pageviews", dimensions = "ga:pageTitle, ga:date",
                 segment = "gaid::xiUv9d6sS3u107dzsIeNbg")



dt3 = ga$getData(id, start.date = "2017-04-01", end.date = "2017-06-30",
                 metrics = "ga:sessions,ga:newUsers,ga:users,ga:uniquePageviews,ga:pageviews,ga:timeOnPage",
                 dimensions = "ga:pageTitle",
                 segment = "gaid::xiUv9d6sS3u107dzsIeNbg")
dt3 = with(dt3, 
           aggregate(list(sessions = sessions, newUsers = newUsers, timeOnPage = timeOnPage,
                          users = users, uniquePageviews = uniquePageviews, pageviews = pageviews),
                     list(pageTitle = pageTitle), sum))
dt3$ave = dt3$timeOnPage/dt3$pageviews
dt3$ave = seconds_to_period(dt3$ave)
dt3$percentage = dt3$newUsers/dt3$users

dt2 = ga$getData(id, start.date = "2017-04-01", end.date = "2017-06-30",
                 metrics = "ga:sessions,ga:percentNewSessions,ga:bounceRate,ga:pageviewsPerSession",
                 dimensions = "ga:sourceMedium",
                 segment = "gaid::xiUv9d6sS3u107dzsIeNbg",
                 batch = TRUE, walk = TRUE)
temp = ga$getData(id, start.date = "2017-04-01", end.date = "2017-06-30",
                  metrics = "ga:sessions,ga:percentNewSessions,ga:bounceRate,ga:pageviewsPerSession",
                  dimensions = "ga:sourceMedium",
                  segment = "gaid::xiUv9d6sS3u107dzsIeNbg", walk = TRUE)
dt4 = ga$getData(id, start.date = "2017-04-01", end.date = "2017-06-30",
                 metrics = "ga:sessions",
                 dimensions = "ga:sourceMedium",
                 segment = "gaid::xiUv9d6sS3u107dzsIeNbg")
dt4$sourceMedium = tolower(dt4$sourceMedium)

temp = with(dt4,
           aggregate(list(sessions = sessions), list(sourceMedium = sourceMedium), sum))
temp$percent = temp$newSession/temp$sessions*100
temp = subset(temp, sessions > 25)
write.csv(temp, "traffic.csv")
