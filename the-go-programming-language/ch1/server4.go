package main

import (
	"ch1"
	"log"
	"net/http"
	"strconv"
)

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	cycles, err := strconv.Atoi(r.URL.Query().Get("cycles"))
	if err != nil {
		cycles = 5
	}
	ch1.Lissajous2(w, float64(cycles))
}
