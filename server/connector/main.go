package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Print("启动连接器")
	addr := net.TCPAddr{IP: net.IPv4zero, Port: 8888}
	listener, err := net.ListenTCP("tcp", &addr)
	if err != nil {
		return
	}

	for true {
		tcpConn, err := listener.AcceptTCP()
		fmt.Println("-------------------- new session --------------------")
		if err != nil {
			continue
		}

		go func() {
			bytes := make([]byte, 512)
			n, err := tcpConn.Read(bytes)
			if err != nil {
				return
			}
			if n > 0 {
				fmt.Printf("收到消息:%s", string(bytes))
			}
		}()
	}
}
