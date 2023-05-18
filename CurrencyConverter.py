
import myfunctions as mf

# Core Program
running = True

while running:
    selected_menu = mf.print_menu()

    if selected_menu == 'q' or selected_menu == 'Q':
        running = False

    running = mf.access_menu(selected_menu)

mf.goodbye()
