package main

import (
  "bufio"
  "fmt"
  "io"
  "log"
  "os"
  "strings"
)

var debug bool

func check(e error) {
  if e != nil {
    fmt.Println("before fatal")
    log.Fatal(e)
    fmt.Println("after fatal") // this will never be printed
    //panic(e)
  }
}

func Smallestrep(line string) int {
  line = strings.TrimSpace(line)
  if debug {
    fmt.Printf("len of line = %d\n", len(line))
    fmt.Printf("count of %q = %d\n", line[0:1], strings.Count(line, line[0:1]))
  }
  if strings.Count(line, line[0:1]) == len(line) {
    return 1
  } else {
    total_len := len(line)
    max_snippet := total_len / 2
    start_index := 0
    start_len := 2
    for {
      snippet := line[start_index:start_len]
      if debug {
        fmt.Println(snippet)
      }

      freq := strings.Count(line, snippet)
      if freq*(start_len-start_index) == total_len {
        return start_len - start_index
      } else {
        if start_len-start_index >= max_snippet {
          if debug {
            fmt.Println("'beyond half way point")
          }
          return total_len
        }
        if debug {
          fmt.Println("increase by 1")
        }
        start_len += 1
      }
    }
  }
}

func main() {
  args := os.Args[1:]
  fmt.Println(args)

  if len(args) == 0 {
    log.Fatal("No argument provided")
  }

  f, err := os.Open(args[0])
  defer f.Close()
  check(err)

  bf := bufio.NewReader(f)
  for {
    switch line, err := bf.ReadString('\n'); err {
    case nil:
      if debug {
        //fmt.Print("->" + line + "<-")
      }
      if len(strings.TrimSpace(line)) == 0 {
        continue
      }
      a := strings.TrimSpace(line)
      if a[0:1] == "#" {
        continue
      }
      fmt.Printf("%d\n", Smallestrep(line))
    case io.EOF:
      return
    default:
      log.Fatal(err)
    }
  }
}
