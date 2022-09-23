// Lissajous generates GIF animations of random Lissajous figures.
package ch1

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
)

var palette = []color.Color{
	color.Black,
	color.RGBA{0xff, 0xff, 0x00, 0xff},
	color.RGBA{0x00, 0xff, 0x00, 0xff},
}

// create constants
const (
	whiteIndex = 0 //first color in palette
	blackIndex = 1 //next color in palette
)

// func main() {
// 	//create a file for output gif image
// 	f, err := os.Create("out.gif")
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer f.Close()
// 	lissajous1(f)
// }

func Lissajous2(out io.Writer, cycles float64) {
	const (
		res     = 0.001 // angular resolution
		size    = 100   // image canvas covers [-size..+size]
		nframes = 64    // number of animation frames
		delay   = 8     // delay between frames in 80ms units
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 //phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		colorIndex := 1
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), uint8(colorIndex))
			colorIndex++
			if colorIndex > len(palette) {
				colorIndex = 1
			}
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) //NOTE: ignoring encoding errors

}

func lissajous1(out io.Writer) {
	Lissajous2(out, 5)
}
