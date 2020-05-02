import random

def comp_sci_chapters():
  chapters = {
    # [Chapter number]: [number of sub-chapter]
    '1.1.1': 5,
    '1.1.2': 3,
    '1.1.3': 4,
    '1.2.1': 8,
    '1.2.2': 6,
    '1.2.3': 3,
    '1.2.4': 5,
    '1.3.1': 4,
    '1.3.2': 6,
    '1.3.3': 5,
    '1.3.4': 4,
    '1.4.1': 10,
    '1.4.2': 3,
    '1.4.3': 5,
    '1.5.1': 4,
    '1.5.2': 1,
    '2.1.1': 4,
    '2.1.2': 4,
    '2.1.3': 4,
    '2.1.4': 3,
    '2.1.5': 2,
    '2.2.1': 6,
    '2.2.2': 6,
    '2.3.1': 6,
  }
  return chapters

def physics_chapters():
  chapters = {
    # [Chapter number]: [number of sub-chapter]
    3: 8,
    4: 9,
    5: 4,
    6: 4,
    7: 5,
    8: 4,
    9: 11,
    10: 6,
    11: 9,
    12: 6,
    13: 4
  }
  return chapters

def pick_chapter(chapters):
  # Gets random key from dictionary of chapters
  main_chapter = random.choice(list(chapters))
  # Gets the sub-chapter from the key
  sub_chapter = random.randint(1, chapters[main_chapter])
  return main_chapter, sub_chapter

def display_chapter(chapters, subject):
  title = ''
  chapter = chapters[subject][0]
  sub_chapter = chapters[subject][1]
  # Changes title according to the subject
  if subject == 'comp sci':
    title = 'Computer science'
  elif subject == 'physics':
    title = 'Physics'
  else:
    print('Something has gone terribly wrong...')
  # Outputs the respective chapters
  print(title)
  print('Chapter: {}'.format(chapter))
  print('Sub-chapter: {}\n'.format(sub_chapter))

def main():
  picked_chapters = {
    # Picks random chapter and sub-chapter for comp sci and physics
    'comp sci': pick_chapter(comp_sci_chapters()),
    'physics': pick_chapter(physics_chapters())
  }
  # Outputs chapters
  display_chapter(picked_chapters, 'comp sci')
  display_chapter(picked_chapters, 'physics')

main()
