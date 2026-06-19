from loader import load_data
from cleaner import clean_data
from analyzer import analyze_data
from visualizer import visualize_data
from exporter import export_data

def main():
    df = load_data()
    if df is None:
        return

    df = clean_data(df)
    df, analysis = analyze_data(df)
    visualize_data(df)
    export_data(df, analysis)

    print("Project completed successfully!")

if __name__ == "__main__":
    main()