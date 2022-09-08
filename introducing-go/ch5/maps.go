package main

import "fmt"

func main() {
	var countryCapitalMap map[string]string

	countryCapitalMap = make(map[string]string)

	countryCapitalMap["Afghanistan"] = "Kabul"
	countryCapitalMap["Albania"] = "Tirana"
	countryCapitalMap["Algeria"] = "Algiers"

	fmt.Println(countryCapitalMap)

	delete(countryCapitalMap, "Algeria")

	fmt.Println(countryCapitalMap)

	indiaStateCapitalMap := map[string]string{
		"Andhra Pradesh":    "Amaravati",
		"Arunachal Pradesh": "Itanagar",
		"Assam":             "Dispur",
		"Bihar":             "Patna",
		"Chhattisgarh":      "Naya Raiput",
		"Goa":               "Panaji",
		"Gujarat":           "Gandhinagar",
	}

	fmt.Println(indiaStateCapitalMap)
	value, ok := indiaStateCapitalMap["Tamil Nadu"]

	if ok {
		fmt.Println(value)
	} else {
		fmt.Println("Lookup failed.")
	}

	value, ok = indiaStateCapitalMap["Gujarat"]

	if ok {
		fmt.Println(value)
	} else {
		fmt.Println("Lookup failed.")
	}
}
