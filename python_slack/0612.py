import slackweb 


comment = "pythonからslackさんへ"

slack = slackweb.Slack(url ="https://hooks.slack.com/services/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")
slack.notify(text = comment)