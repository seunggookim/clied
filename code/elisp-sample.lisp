(defun count-words-in-buffer ()
  "Count the number of words in the current buffer."
  (interactive)
  (save-excursion
    (let ((count 0))
      (goto-char (point-min))
      (while (< (point) (point-max))
        (forward-word 1)
        (setq count (1+ count)))
      (message "Number of words in buffer: %d" count))))
