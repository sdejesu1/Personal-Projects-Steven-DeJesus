#Author: Steven De Jesus

wins = 0
losses = 0
# define main
def main():
    # call display title
    display_title()
    # call count_results, set to two variables bc two variables will be returned
    main_wins, main_losses = count_results()
    # after count_results runs and i have tallies
    # call show_results and pass those two variables from count
    show_results(main_wins, main_losses)
    
# define count_results
def count_results():
    wins = 0
    losses = 0
    # open analysis_data.txt and read file
    read_analysis = open('analysis_data.txt', 'r')
    # read each line
    line = read_analysis.readline()
    line = line.rstrip()
    # for loop to keep reading the lines
    for line in read_analysis:
        line = str(line.rstrip())
        if line == "Won":
            wins += 1
        elif line == "Lost":
            losses += 1
    return wins, losses

    # close file
    read_analysis.close()
            
# define show_results
def show_results(show_wins, show_losses):
    print('Number of Simulations: 100')
    print(f'(+) Wins: {show_wins}')
    print(f'(-) Losses: {show_losses}' + '\n')
    print(f'You won {show_wins / 100:.2f}% of the time')

# define display title
def display_title():
    print('----------------------')
    print('Shut the Box: Analysis')
    print('----------------------')

main()
