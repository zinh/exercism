package protein

const testVersion = 1

var CodonMap = map[string]string{
	"AUG": "Methionine",
	"UUU": "Phenylalanine", "UUC": "Phenylalanine",
	"UUA": "Leucine", "UUG": "Leucine",
	"UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
	"UAU": "Tyrosine", "UAC": "Tyrosine",
	"UGU": "Cysteine", "UGC": "Cysteine",
	"UGG": "Tryptophan",
	"UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
}

func FromCodon(codon string) string {
	return CodonMap[codon]
}

func FromRNA(rna string) (proteins []string) {
	r := []rune(rna)
	for i := 0; i <= len(r)/3-1; i++ {
		code := string([]rune{r[3*i], r[3*i+1], r[3*i+2]})
		if CodonMap[code] == "STOP" {
			return proteins
		}
		proteins = append(proteins, CodonMap[code])
	}
	return proteins
}
