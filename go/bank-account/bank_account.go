package account

const testVersion = 1

type Account struct {
  balance int64
  closed bool
}

type AccountIf interface {
  Close() (int64, bool)
  Balance() (int64, bool)
  Deposit(int64) (int64, bool)
}

func (a Account) Close() (int64, bool) {
  if a.closed {
    return 0, false
  }
  c := a.balance
  a = Account{0, true}
  return c, true
}

func (a Account) Balance() (int64, bool) {
  if a.closed {
    return 0, false
  }
  return a.balance, true
}

func (a Account) Deposit(deposit int64) (int64, bool) {
  if a.closed {
    return 0, false
  }

  a.balance += deposit
  return a.balance, true
}

func Open(deposit int64) *Account {
  if deposit < 0 {
    return nil
  } 
  return &Account{ deposit, false }
}
