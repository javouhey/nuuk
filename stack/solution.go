package main

import (
  "bufio"
  "fmt"
  "io"
  "log"
  "os"
  "errors"
  "strings"
  "strconv"
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

type PushPopInts interface {
    Push(item int)
    Pop() (int, error)
}

type Stack struct {
    storage []int
    count int
}

func NewStack() *Stack {
    s := Stack{make([]int, 1), 0}
    return &s
}

func (s *Stack) Pop() (int, error) {
    if s.count == 0 {
        return 0, errors.New("stack: empty")
    } else {
        retval := s.storage[s.count - 1]
        s.count = s.count - 1
        if s.count != 0 {
            s.storage = s.storage[0:s.count]
        } else {
            s.storage[0] = 0
        }
        return retval, nil
    }
}

func (s *Stack) Push(item int) {
    if s.count == 0 {
        s.storage[0] = item
        s.count = s.count + 1
    } else {
        s.storage = append(s.storage, item)
        s.count = s.count + 1
    }
}

func (s *Stack) String() string {
    return fmt.Sprint([]int(s.storage))
}

func Stackpopper(line string) string {
    st := NewStack()
    line = strings.TrimSpace(line)
    parts := strings.Split(line, " ")
    for _, value := range parts {
        ani, err := strconv.Atoi(strings.TrimSpace(value))
        if err != nil {
            continue
        }
        st.Push(ani)
    }

    g := make([]int, 0)
    flag := true
    for {
        item, err := st.Pop()
        if err != nil {
            break
        }
        if flag {
            g = append(g, item)
        } 
        flag = !flag
    }

    retval := " "
    for _, v := range g {
        retval = retval + strconv.Itoa(v) + " "
    }
    return strings.TrimSpace(retval)
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
      fmt.Printf(Stackpopper(line))
    case io.EOF:
      return
    default:
      log.Fatal(err)
    }
  }
}
