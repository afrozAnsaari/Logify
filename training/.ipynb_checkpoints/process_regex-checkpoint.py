{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e6cb2ee-8829-4f42-881d-b5883c61f7cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "def classify_with_regex(log_message:str):\n",
    "    regex_patterns = {\n",
    "        r\"User User\\d+ logged (in|out).\": \"User Action\",\n",
    "        r\"Backup (started|ended) at .*\": \"System Notification\",\n",
    "        r\"Backup completed successfully.\": \"System Notification\",\n",
    "        r\"System updated to version .*\": \"System Notification\",\n",
    "        r\"File .* uploaded successfully by user .*\": \"System Notification\",\n",
    "        r\"Disk cleanup completed successfully.\": \"System Notification\",\n",
    "        r\"System reboot initiated by user .*\": \"System Notification\",\n",
    "        r\"Account with ID .* created by .*\": \"User Action\"\n",
    "    }\n",
    "    for pattern, label in regex_patterns.items():\n",
    "        if re.search(pattern, log_message, re.IGNORECASE):\n",
    "            return label\n",
    "    return None    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python(logify)",
   "language": "python",
   "name": "logify311"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
