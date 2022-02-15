package main

import "fmt"

var KEY = []byte{
	11, 32, 43, 45, 67, 23, 45, 67, 7, 8, 8, 9, 7, 6, 44, 55, 66, 77, 16, 75,
	98, 9, 12, 3, 4, 5, 6, 7, 6, 5, 8, 77, 3, 5, 7, 22, 33, 44, 52, 64,
	75, 82, 98, 107, 113, 125, 4, 32, 99, 122, 11, 32, 43, 45, 67, 23, 45, 67, 7, 8,
	8, 9, 7, 6, 44, 55, 66, 77, 16, 75, 98, 9, 12, 3, 4, 5, 6, 7, 6, 5,
	8, 77, 3, 5, 7, 22, 33, 44, 52, 64, 75, 82, 98, 107, 113, 125, 4, 32, 99, 122,
}

var LK = len(KEY)

func Encoder(data []byte, n int) {
	Decoder(data, n)
}

func Decoder(data []byte, n int) {
	lp, ll := loopTimes(n)
	var base int
	for i := 0; i < lp; i++ {
		base = i * LK
		for j := 0; j < LK; j++ {
			data[j+base] ^= KEY[j]
		}
	}

	base = lp * LK
	for i := 0; i < ll; i++ {
		data[i+base] ^= KEY[i]
	}
	fmt.Println(string(data[:n]))
}

func loopTimes(n int) (int, int) {
	return n / LK, n % LK
}
