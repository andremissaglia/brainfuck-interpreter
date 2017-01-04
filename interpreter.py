#!/bin/python
import sys


class Node:
    value = 0
    prv = None
    nxt = None

    def right(self):
        if not self.nxt:
            self.nxt = Node()
            self.nxt.prv = self
        return self.nxt

    def left(self):
        if not self.prv:
            self.prv = Node()
            self.prv.nxt = self
        return self.prv


def run(code):
    tape = Node()
    stack = []
    code = code
    l = len(code)
    pc = 0
    jumps = {}

    # Preprocessing jumps
    for i in range(l):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            last = stack.pop()
            jumps[last] = i
            jumps[i] = last

    # Executing
    while pc != l:
        symbol = code[pc]
        if symbol == '+':
            tape.value += 1
        elif symbol == '-':
            tape.value -= 1
        elif symbol == '>':
            tape = tape.right()
        elif symbol == '<':
            tape = tape.left()
        elif symbol == ',':
            tape.value = ord(sys.stdin.read(1))
        elif symbol == '.':
            sys.stdout.write(chr(tape.value))
            sys.stdout.flush()
        elif symbol == '[':
            if tape.value == 0:
                pc = jumps[pc]
        elif symbol == ']':
            if tape.value != 0:
                pc = jumps[pc]

        pc += 1


if len(sys.argv) != 2:
    print("Usage: python {} <file>".format(sys.argv[0]))
    exit(-1)


with open(sys.argv[1]) as f:
    code = f.read()

run(code)
