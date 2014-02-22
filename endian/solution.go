package main

import (
  "fmt"
  "log"
)

var debug bool

func check(e error) {
  if e != nil {
    fmt.Println("before fatal")
    log.Fatal(e)
    fmt.Println("after fatal") // this will never be printed
  }
}

func Endian() string {
  var i uint8
  var g uint32
  g = 0x90AB12CD
  i = uint8(g)
  //fmt.Println("hello", g, &g, i)
  if i == 205 {
      return "LittleEndian"
  } else {
      return "BigEndian"
  }
}

func main() {
    fmt.Println(Endian())
}
