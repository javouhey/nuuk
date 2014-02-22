package main

import (
    "testing"
)

func TestStackpopper(t *testing.T) {
    if Stackpopper("1 2 3 4") != "4 2" {
        t.Fatalf("expected ..0")
    }
    if Stackpopper("10 -2 3 4") != "4 -2" {
        t.Fatalf("expected ..1")
    }
}
