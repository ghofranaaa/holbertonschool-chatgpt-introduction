#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mines = set(random.sample(range(self.total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.remaining_cells = self.total_cells - mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        print(f"Revealing cell ({x}, {y})")
        if (y * self.width + x) in self.mines:
            print("Hit a mine")
            return False
        if self.revealed[y][x]:
            print("Already revealed")
            return True
        self.revealed[y][x] = True
        self.remaining_cells -= 1
        if self.remaining_cells == 0:
            print("Congratulations! You won the game!")
            return False
        if self.count_mines_nearby(x, y) == 0:
            print("No neighboring mines, revealing adjacent cells")
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        try:
            while True:
                self.print_board()
                if self.remaining_cells == 0:
                    print("Congratulations! You won the game!")
                    break
                try:
                    x = int(input("Enter x coordinate: "))
                    y = int(input("Enter y coordinate: "))
                    if not (0 <= x < self.width and 0 <= y < self.height):
                        print("Coordinates out of bounds. Please enter valid coordinates.")
                        continue
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
        except KeyboardInterrupt:
            print("\nGame aborted.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
