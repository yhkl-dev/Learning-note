package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

/*
	这个过程并不是原子得
	1.从内存中读出n
	2.执行++
	3.再赋值结果

	这个过程中，其他协程也会进来读取n的值，因此不是原子的

	所谓的原子，执行过程中不会发生上下文切换
*/
func main() {
	fmt.Println("vim-go")
	var n int32 = 0
	wg := sync.WaitGroup{}
	for i := 0; i < 1000000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			atomic.AddInt32(&n, 1)
		}()
	}
	wg.Wait()
	fmt.Println(n)
}
