package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	Name            string  `json:"name"`
	TechnicalSkills float64 `json:"Technical Skills"`
	SoftSkills      float64 `json:"Soft Skills"`
	BusinessSkills  float64 `json:"Business Skills"`
	CreativeSkills  float64 `json:"Creative Skills"`
	AcademicSkills  float64 `json:"Academic Skills"`
}

type People struct {
	People []Person `json:"people"`
}

func main() {
	// Read the JSON file
	jsonBytes, err := os.ReadFile("../fulldata/data2.json")
	if err != nil {
		fmt.Println("read file error:", err)
		return
	}

	var people People
	if err := json.Unmarshal(jsonBytes, &people); err != nil {
		fmt.Println("unmarshal error:", err)
		return
	}

	// Create a CSV file
	csvFile, err := os.Create("data3.csv")
	if err != nil {
		fmt.Println("create csv error:", err)
		return
	}
	defer csvFile.Close()

	writer := csv.NewWriter(csvFile)
	defer func() {
		writer.Flush()
		if err := writer.Error(); err != nil {
			fmt.Println("csv write error:", err)
		}
	}()

	// Write header
	if err := writer.Write([]string{
		"Name", "Technical Skills", "Soft Skills", "Business Skills", "Creative Skills", "Academic Skills",
	}); err != nil {
		fmt.Println("write header error:", err)
		return
	}

	// Write data
	for _, p := range people.People {
		row := []string{
			p.Name,
			fmt.Sprint(p.TechnicalSkills),
			fmt.Sprint(p.SoftSkills),
			fmt.Sprint(p.BusinessSkills),
			fmt.Sprint(p.CreativeSkills),
			fmt.Sprint(p.AcademicSkills),
		}
		if err := writer.Write(row); err != nil {
			fmt.Println("write row error:", err)
			return
		}
	}
}
