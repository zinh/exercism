package space

type Planet string

func Age(second float64, planet Planet) (result float64){
  s := map[Planet]float64{
    "Earth": 31557600,
    "Mercury": 7600543.81992,
    "Venus": 19414149.052176,
    "Mars": 59354032.69008,
    "Jupiter": 374355659.124,
    "Saturn": 929292362.8848,
    "Uranus": 2651370019.3296,
    "Neptune": 5200418560.032,
  }
  second_per_year := s[planet]
  result = second / second_per_year
  return result
}
