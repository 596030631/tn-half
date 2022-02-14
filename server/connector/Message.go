package main

import (
	"encoding/json"
	"fmt"
)

type MessageInfo struct {
	SourceId string   `json:"sourceId"`
	Body     []string `json:"body"`
}

type MessageReceiverInfo struct {
	Sender   string   `json:"sender"`
	Receiver string   `json:"receiver"`
	Body     []string `json:"body"`
}

type MessagePublishInfo struct {
	UserId string `json:"user_id"`
}

var sessionMap = map[string]MessageInfo{}

func MessageExist(id string) bool {
	_, ok := sessionMap[id]
	return ok
}

func MessageArrived(js []byte) {
	var body MessageReceiverInfo
	err := json.Unmarshal(js, &body)
	if err != nil {
		fmt.Println(err)
		return
	}
	if v, ok := sessionMap[body.Receiver]; ok {
		v.Body = append(v.Body, body.Body...)
		sessionMap[body.Receiver] = v
	} else {
		sessionMap[body.Receiver] = MessageInfo{SourceId: body.Receiver, Body: body.Body}
	}
}

func MessagePublish(dest []byte) MessageInfo {
	var js MessagePublishInfo
	err := json.Unmarshal(dest, &js)
	if err != nil {
		return MessageInfo{}
	}
	r := sessionMap[js.UserId]
	messageClear(js.UserId)
	return r
}

func messageClear(dest string) {
	delete(sessionMap, dest)
}
