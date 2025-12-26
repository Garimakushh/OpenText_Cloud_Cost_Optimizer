from rich import print
from profile_extractor import extract_profile
from billing_generator import generate_billing
from cost_analyzer import analyze_cost
from report_exporter import export_html

def main():
    while True:
        print("\n[bold cyan]Cloud Cost Optimizer[/bold cyan]")
        print("1. Enter project description")
        print("2. Generate synthetic billing data")
        print("3. Run cost analysis & recommendations")
        print("4. View cost optimization report")
        print("5. Export HTML report")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            desc = input("\nEnter description:\n")
            extract_profile(desc)
            print("✔ Project profile generated")

        elif choice == "2":
            generate_billing()
            print("✔ Billing data generated")

        elif choice == "3":
            analyze_cost()
            print("✔ Cost analysis completed")

        elif choice == "4":
            print(open("cost_optimization_report.json").read())

        elif choice == "5":
            export_html()
            print("✔ HTML report exported")

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
