def start():
    import os
    import codecs
    import pyperclip
    import PySimpleGUI as sg

    global output_result

    # For linux needs package pyperclip
    # We need to fix encoding to UTF-8
    dir_path = "/home/jil/ulumislam"

        # implementation code here
    def search_concordance(word, page_num=1):
        global output_result
        results = []
        for root, dirs, files in os.walk(dir_path):
            for filename in files:
                if filename.endswith('.txt'):
                    # Check if the filename contains the user's input word
                    if word.lower() in filename.lower():
                        # If there is a match, open the file and read its contents
                        with codecs.open(os.path.join(root, filename), 'r', 'utf-8') as file:
                            contents = file.read()
                            # Add the file contents to the results list
                            results.append(contents)
        if len(results) == 0:
            sg.popup("Your word is not found, try another similar word. Silakan ketik hanya satu kata di sini")
        else:
            num_pages = (len(results) - 1) // 10 + 1  # Calculate the number of pages
            if page_num > num_pages:  # Make sure page number is not out of range
                page_num = num_pages
            start_index = (page_num - 1) * 10
            end_index = start_index + 10
            results_page = results[start_index:end_index]
            output_result.update(value="\n\n".join(results_page))
            output_result.set_focus()

    def copy_text():
        text_to_copy = output_result.get()
        pyperclip.copy(text_to_copy)

    layout = [
        [sg.Text("Please type any only one word here:"), sg.Input(key="-WORD-"), sg.Button("Search", bind_return_key=True), sg.Button("Copy to Clipboard")],
        [sg.Text("The result in GUI output result is here:")],
        [sg.Multiline(key="-OUTPUT-", size=(100, 30), disabled=True, autoscroll=True)],
    ]

    window = sg.Window("©2023 Abdullahghumari.com The Largest Quran and Hadith Chatpot Concordance", layout)

    output_result = window['-OUTPUT-']

    #if event == "Search":
    #    search_concordance(values["-WORD-"], page_num=1)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "Search":
            search_concordance(values["-WORD-"])
        if event == "Copy to Clipboard":
            copy_text()

    window.close()