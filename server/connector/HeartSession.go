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
	buffer := make([]byte, 512)
	for {
		n, raddr, err := heartListener.ReadFromUDP(buffer)
		if err != nil {
			continue
		}
		userId := string(buffer[:n])
		fmt.Printf("remote<%s> userId:%s\n", raddr.String(), userId)

		flag := messageEmpty
		if MessageExist(userId) {
			flag = messageExist
		}
		_, _ = heartListener.WriteToUDP([]byte{flag}, raddr)
	}
}
