package main

import (
	"fmt"
	"net"
)

const messageEmpty byte = 0
const messageExist byte = 1

func HeartCreate() {
	fmt.Println("---------------------- Start Heart ---------------------------")

	laddr := net.UDPAddr{IP: net.IPv4zero, Port: 9999}
	heartListener, err := net.ListenUDP("udp4", &laddr)
	if err != nil {
		fmt.Println("---------------------- Heart Start Error ---------------------------")
		return
	}

	for {
		bytes := make([]byte, 64)
		n, raddr, err := heartListener.ReadFromUDP(bytes)
		if err != nil {
			continue
		}
		userId := string(bytes[:n])
		fmt.Printf("remote<%s> userId:%s\n", raddr.String(), userId)
		flag := messageEmpty
		var ok bool
		if _, ok = SessionMap[userId]; ok {
			flag = messageExist
		}
		_, _ = heartListener.WriteToUDP([]byte{flag}, raddr)
	}
}
