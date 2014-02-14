package main

import (
    "testing"
)

func TestSmallestRepetition(t *testing.T) {
    if Smallestrep("d") != 1 {
        t.Fatalf("expected 1")
    }
    if Smallestrep("dd") != 1 {
        t.Fatalf("expected 1")
    }
    if Smallestrep("ddd") != 1 {
        t.Fatalf("expected 1")
    }
    if Smallestrep("dad") != 3 {
        t.Fatalf("expected 3")
    }
    if Smallestrep("xyxyxy") != 2 {
        t.Fatalf("expected 2")
    }
    if Smallestrep("xyzxyz") != 3 {
        t.Fatalf("expected 3")
    }
    if Smallestrep("xyzxyzxyzp") != 10 {
        t.Fatalf("expected 10")
    }
    if Smallestrep("jklmnopjklmnopjklmnopjklmnopjklmnopjklmnopjklmnop") != 7 {
        t.Fatalf("expected 7")
    }
}
