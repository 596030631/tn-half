package main

import (
	"encoding/json"
	"fmt"
	"net"
)

func SessionReceiveCreate() {
	go func() {
		fmt.Println("------------------- start receiver --------------------------")
		addr := net.TCPAddr{IP: net.IPv4zero, Port: 8888}
		listener, err := net.ListenTCP("tcp", &addr)
		if err != nil {
			return
		}
		buffer := make([]byte, 4096)
		for {
			conn, e1 := listener.AcceptTCP()
			fmt.Println("-------------------- new session --------------------")
			if e1 != nil {
				continue
			}
			n, e2 := conn.Read(buffer)
			if e2 != nil {
				continue
			}
			if n > 0 {
				Decoder(buffer, n)
				j := string(buffer[:n])
				fmt.Printf("\nReceiver >>> %s\n", j)
				MessageArrived(buffer[:n])
			}
			_ = conn.Close()
		}
	}()
}

func SessionPublishCreate() {
	go func() {
		fmt.Println("------------------- start publisher --------------------------")
		addr := net.TCPAddr{IP: net.IPv4zero, Port: 8889}
		listener, err := net.ListenTCP("tcp", &addr)
		if err != nil {
			return
		}
		buffer := make([]byte, 4096)
		for {
			conn, e1 := listener.AcceptTCP()
			fmt.Println("-------------------- new session --------------------")
			if e1 != nil {
				continue
			}
			n, e2 := conn.Read(buffer)
			if e2 != nil {
				continue
			}
			if n > 0 {
				Decoder(buffer, n)
				fmt.Printf("Data:%s\n", string(buffer[:n]))
				if n > 2 {
					b, _ := json.Marshal(MessagePublish(buffer[:n]))
					Encoder(b, len(b))
					_, _ = conn.Write(b)
				}
			}
			_ = conn.Close()
		}
	}()
}
