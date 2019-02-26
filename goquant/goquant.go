package main

import (
	"fmt"
	"image"
	"os"
	"time"

	"golang.org/x/image/bmp"
)

func quantize(img image.Image, x int, y int) {
	r, g, b, a := img.At(x, y).RGBA()
	fmt.Println(r/256, g/256, b/256, a/256)
}

func main() {
	init := time.Now()
	defer func() {
		end := time.Now()
		fmt.Println("Total time:", end.Sub(init))
	}()
	file, err := os.Open("../input.bmp")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	img, err := bmp.Decode(file)
	if err != nil {
		panic(err)
	}
	fmt.Println(img.Bounds().Dx())
	fmt.Println(img.Bounds().Dy())
	fmt.Println(img.At(0, 0))
	for x := 0; x < img.Bounds().Dx(); x++ {
		for y := 0; y < img.Bounds().Dy(); y++ {
			go quantize(img, x, y)
		}
	}
}
