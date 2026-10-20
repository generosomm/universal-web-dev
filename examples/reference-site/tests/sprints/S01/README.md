# S01 tests

Run from the site folder: `python -m unittest discover -s tests -t .` (the tide checks need Node and skip without it).

| Acceptance | Test or check |
| --- | --- |
| h1, sentence, one action | `test_first_screen_says_what_it_is`; browser walk-through |
| Rooms and booking emails | `test_booking_uses_email_not_a_fake_checkout` |
| Tide windows, midnight | `TideModel` tests |
| Sample label, no-script answer | `test_tide_has_a_no_script_answer_and_a_warning` |
| Images, headings, links | `test_images_have_alt_and_dimensions`, `test_every_section_is_named_by_a_heading`, `test_internal_links_and_files_resolve` |
| Script loads at all | `test_script_is_a_classic_script` |
| No scroll, targets, contrast, focus | manual browser checks recorded in [S01](../../../docs/sprints/S01.md) |

Not covered: physical devices, screen readers, performance measurement.
