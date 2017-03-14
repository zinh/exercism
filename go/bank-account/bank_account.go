package account

import "sync"

const testVersion = 1

type Account struct {
	balance int64
	closed  bool
	mutex   *sync.Mutex
}

type AccountIf interface {
	Close() (int64, bool)
	Balance() (int64, bool)
	Deposit(int64) (int64, bool)
}

func (a *Account) Close() (int64, bool) {
	a.mutex.Lock()
	if a.closed {
		a.mutex.Unlock()
		return 0, false
	}
	c := a.balance
	a.balance = 0
	a.closed = true
	a.mutex.Unlock()
	return c, true
}

func (a *Account) Balance() (int64, bool) {
	if a.closed {
		return 0, false
	}
	return a.balance, true
}

func (a *Account) Deposit(deposit int64) (int64, bool) {
	if a.closed {
		return 0, false
	}

	a.mutex.Lock()
	newBalance := a.balance + deposit
	if newBalance >= 0 {
		a.balance = newBalance
		a.mutex.Unlock()
		return a.balance, true
	}
	a.mutex.Unlock()
	return 0, false
}

func Open(deposit int64) *Account {
	if deposit < 0 {
		return nil
	}
	return &Account{deposit, false, &sync.Mutex{}}
}
