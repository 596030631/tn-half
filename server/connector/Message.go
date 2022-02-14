package main

import "strings"

var SessionMap = map[string]string{}

func MessageArrived(msg string) {
	arr := strings.Split(msg, ",")
	if len(arr) == 3 {
		dest := arr[1]
		SessionMap[dest] = strings.Join(arr[1:], ",")
	} else {
		print("消息格式错误")
	}
}

func MessagePublish(dest string) string {
	return SessionMap[dest]
}

func MessageClear(dest string) {
	delete(SessionMap, dest)
}
