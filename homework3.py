def read_transactions(filename):
    totals = {}
    try:
        with open(filename, "r") as file:
             for line in file :
                 line = line.strip()
                 if not line:
                     continue
                 name, amount = line.split(",")
                 amount = float(amount)
                 if name in totals:
                     totals[name] += amount
                 else:
                     totals[name] = amount
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return {}
    return totals
def main():
    filename  ="homework3.txt"
    totals = read_transactions(filename)
    sorted_totals = sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    )
    print("\n--- Transaction summary (sorted Highest First)---")
    for customer, total in sorted_totals:
        print(f"{customer}: ${total:.2f}")
    with open("report.txt","w")as report:
        for customer, total in sorted_totals:
            report.write(f"{customer}:${total:.2f}\n")
    print("\nSuccess! Results have been printedabove and saved to report.txt")        
if __name__ == "__main__":
       main()
              
