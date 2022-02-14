package main

import (
	"fmt"
	"net"
)

const messageReceive byte = '0' // 客户端发送消息
const messagePublish byte = '1' // 客户端读取消息

type Session struct {
}

func SessionCreate() {
	go func() {
		fmt.Println("------------------- start receiver --------------------------")
		addr := net.TCPAddr{IP: net.IPv4zero, Port: 8888}
		listener, err := net.ListenTCP("tcp", &addr)
		if err != nil {
			return
		}
		for {
			conn, e1 := listener.AcceptTCP()
			fmt.Println("-------------------- new session --------------------")
			if e1 != nil {
				continue
			}
			bytes := make([]byte, 128)
			n, e2 := conn.Read(bytes)
			if e2 != nil {
				continue
			}
			if n > 0 {
				fmt.Printf("Data:%s\n", string(bytes[:n]))

				switch bytes[0] {
				case messageReceive:
					msg := string(bytes[2:n])
					fmt.Printf("消息内容:%s\n", msg)
					MessageArrived(msg)
					break
				case messagePublish:
					if n > 2 {
						dst := string(bytes[2:n])
						_, _ = conn.Write([]byte(MessagePublish(dst)))
						MessageClear(dst)
					}
					break
				}
			}
			_ = conn.Close()
		}
	}()
}
