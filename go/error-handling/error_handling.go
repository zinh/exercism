package erratum

const testVersion = 2

func Use(o ResourceOpener, input string) error {
  resource, err := o()
  defer func(){
    r := recover()
    if _, ok := r.(FrobError); ok {
      resource.Defrob(r.defrobTag)
    }
    resource.Close()
    return r
  }()
  if err != nil {
    return err
  }
  resource.Frob(input)
  return nil
}
