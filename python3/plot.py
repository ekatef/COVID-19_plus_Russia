#!/usr/bin/env python

if __name__ == '__main__':
  import matplotlib
  matplotlib.use('Agg')

from covid19ru.plot import plot, plot_sliding

def plot_all():
  plot(show=True, save_name='ruscovid.png', labels_in_russian=False,
       min_threshold=30, rng=(None,10), title_suffix=', Top-10')
  plot(show=True, save_name='ruscovid_10_20.png', labels_in_russian=False,
       min_threshold=30, rng=(10,20), title_suffix=', Places 11..21', right_margin=1)
  plot(show=True, save_name='ruscovid_ru.png', labels_in_russian=True,
       min_threshold=30, rng=(None,10), title_suffix=', первая десятка')
  plot(show=True, save_name='ruscovid_ru_10_20.png', labels_in_russian=True,
       min_threshold=30, rng=(10,20), title_suffix=', места 11..21', right_margin=1)

  plot_sliding(show=True, save_name='ruscovid_ma.png', labels_in_russian=False,
       min_threshold=10, rng=(None,10), title_suffix=', Top-10')
  plot_sliding(show=True, save_name='ruscovid_ma_10_20.png', labels_in_russian=False,
       min_threshold=10, rng=(10,20), title_suffix=', Places 11..21', right_margin=1)
  plot_sliding(show=True, save_name='ruscovid_ru_ma.png', labels_in_russian=True,
       min_threshold=10, rng=(None,10), title_suffix=', первая десятка')
  plot_sliding(show=True, save_name='ruscovid_ru_ma_10_20.png', labels_in_russian=True,
       min_threshold=10, rng=(10,20), title_suffix=', места 11..21', right_margin=1)


if __name__ == '__main__':
  plot_all()

