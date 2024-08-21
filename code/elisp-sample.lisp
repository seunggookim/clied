- Use Ctrl-w followed by h, j, k, or l to navigate between splits.
(defun count-words-in-buffer ()
- Use Ctrl-w followed by h, j, k, or l to navigate between splits.
  "Count the number of words in the current buffer."
  (interactive)
  (save-excursion
    (let ((count 0))
      (goto-char (point-min))
      (while (< (point) (point-max))
        (forward-word 1)
        (setq count (1+ count)))
      (message "Number of words in buffer: %d" count))))
