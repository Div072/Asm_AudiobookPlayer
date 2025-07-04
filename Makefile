# Makefile for VLC Audiobook Player

# Variables
VENV = env
PYTHON = python3
SRC = CLI.commands  # Path to main player script
AUDIO_FILE ?= test.mp3  # Default audio file
COMMAND = play  # Default command to run
DUMMY = CLI.dummy
# Default target
all: run
env:
	@echo "Activating virtual environment..."
	 .$(VENV)/bin/activate
	@echo "Virtual environment activated."

	

# Run the player
run: 
	@echo "Starting player with $(AUDIO_FILE)..."
	$(PYTHON) -m $(SRC)$(COMMAND)
dummy: 
	@echo "Starting player with $(AUDIO_FILE)..."
	$(PYTHON) -m $(DUMMY) $(COMMAND)

# Cleanup
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

nuke: clean
	rm -rf $(VENV)

help:
	@echo "Usage:"
	@echo "  make        - Install dependencies and run player"
	@echo "  make run    - Run player with default audio (test.mp3)"
	@echo "  make run AUDIO_FILE=your_file.mp3 - Run with custom audio"
	@echo "  make clean  - Remove Python cache files"
	@echo "  make nuke   - Full cleanup including virtualenv"

.PHONY: all venv run clean nuke help