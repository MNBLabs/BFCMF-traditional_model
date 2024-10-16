import itertools
import pandas as pd
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def calculate_absolute_differences(frequencies):
    differences = []
    for i, j in itertools.combinations(frequencies, 2):
        differences.append(abs(i - j))
    return differences

def remove_redundancies(differences):
    return sorted(set(differences))

def calculate_reciprocals(differences):
    reciprocals = {d: 1 / d for d in differences}
    return reciprocals

def generate_time_stamps(reciprocals):
    time_stamps_dict = {}
    for diff, reciprocal in reciprocals.items():
        n = 1
        time_stamps_dict[diff] = []
        while (n * reciprocal) <= 1:
            # Format time stamps to have consistent decimal places
            time_stamps_dict[diff].append(format(n * reciprocal, ".6f"))
            n += 1
    return time_stamps_dict

def f_traditional_model(frequencies):
    differences = calculate_absolute_differences(frequencies)
    unique_differences = remove_redundancies(differences)
    reciprocals = calculate_reciprocals(unique_differences)
    time_stamps_dict = generate_time_stamps(reciprocals)
    return time_stamps_dict

def plot_beat_table(time_stamps_dict):
    all_time_stamps = sorted(set(itertools.chain(*time_stamps_dict.values())))
    df = pd.DataFrame(all_time_stamps, columns=["Time (s)"])
    
    for diff, stamps in time_stamps_dict.items():
        df[f"{diff} Hz (Beat)"] = df["Time (s)"].apply(lambda x: "Beat" if x in stamps else "")
    
    return df, all_time_stamps

def print_table_with_colors(df):
    headers = df.columns.tolist()
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "+" + "+".join(["-" * (len(h) + 2) for h in headers]) + "+"

    # Print the header with cyan color
    print(separator_line)
    print(Fore.CYAN + header_line)
    print(separator_line)
    
    for index, row in df.iterrows():
        row_str = "| "
        for i, (item, header) in enumerate(zip(row, headers)):
            # Color the first column (Time column) in cyan
            if i == 0:
                row_str += f"{Fore.CYAN}{str(item).ljust(len(header))} | "
            elif index == 0:  # Color the first row (headers) in cyan
                row_str += f"{Fore.CYAN}{str(item).ljust(len(header))} | "
            else:
                # Color "Beat" in red if it coincides in the same row
                if item == "Beat" and row[1:].tolist().count("Beat") > 1:
                    row_str += f"{Fore.RED}{str(item).ljust(len(header))} | "
                elif item == "Beat":  # Non-coinciding "Beat" text in white
                    row_str += f"{Fore.WHITE}{str(item).ljust(len(header))} | "
                else:
                    row_str += f"{str(item).ljust(len(header))} | "
        print(row_str)
        print(separator_line)

def f_traditional_model_user_input():
    while True:
        input_frequencies = input("Enter at least two frequencies separated by commas (or type 'exit' to quit): ").strip()
        
        if input_frequencies.lower() == 'exit':
            print("Model terminated.")
            break

        try:
            frequencies = list(map(int, input_frequencies.split(',')))
            if len(frequencies) < 2:
                raise ValueError("At least two frequencies are required.")
            
            # Remove duplicates from the list
            unique_frequencies = list(set(frequencies))
            if len(unique_frequencies) < 2:
                raise ValueError("Please enter at least two different frequencies.")
            
            frequencies = unique_frequencies

        except ValueError as e:
            print(f"Error: {e}. Please enter valid integers for frequencies.")
            continue

        time_stamps_dict = f_traditional_model(frequencies)
        beat_table, all_time_stamps = plot_beat_table(time_stamps_dict)
        
        print(f"\nFrequencies: {frequencies}")
        print(f"Total unique beats: {len(all_time_stamps)}")
        print(f"Time Stamps: {all_time_stamps}")
        print("Beat Table:")
        print_table_with_colors(beat_table)

if __name__ == "__main__":
    f_traditional_model_user_input()
