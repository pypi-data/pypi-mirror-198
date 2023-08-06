# Volux Audio <!-- omit in toc -->

[![PyPI](https://img.shields.io/pypi/v/voluxaudio?logo=python)](https://pypi.org/project/voluxaudio)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/voluxaudio?logo=Python)](https://pypi.org/project/voluxaudio)
[![PyPI - License](https://img.shields.io/pypi/l/voluxaudio?color=orange&logo=Python)](https://pypi.org/project/voluxaudio)

---

☠️ **EXPERIMENTAL:** - Beware all ye who enter here ☠️

---

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
- [Usage](#usage)
  - [`VoluxAudioStream` - Source](#voluxaudiostream---source)
    - [Non-buffered Example](#non-buffered-example)
    - [Buffered Example](#buffered-example)
    - [Audio-visualization Example](#audio-visualization-example)
- [Todo List](#todo-list)
- [Links](#links)


## Installation 

```bash
pip install voluxaudio
```

## Usage

### `VoluxAudioStream` - Source

#### Non-buffered Example

This Python code uses the `voluxaudio` library to open a new audio stream and calls the `on_data` function every time it gets a new chunk of audio data. The `on_data` function simply prints a message indicating that a new chunk of audio data has been received, along with the current timestamp.

The `CHUNK_SIZE` variable defines the size of each chunk of audio data in bytes, and the `CHANNEL_COUNT` variable defines the number of audio channels.

The code creates a `VoluxAudioStream` object with the `on_data` function, `chunk_size`, and `channels` as arguments. It then enters an infinite loop that keeps the audio stream open and calls `sleep(1)` to wait for one second before checking for new audio data again.

```python
from voluxaudio import VoluxAudioStream
from time import sleep, perf_counter

CHUNK_SIZE = 1024
CHANNEL_COUNT = 2

def on_data(
    in_data, # audio data from this chunk
    frame_count, # number of samples chunk
    time_info,
    status_flags,
    buffer_read_dtype, # buffer's datatype
    channel_count, # number of channels
    sample_rate, # number of samples collected per second
):
    """Do this every time we get a new chunk of data."""
    print(f"got a new chunk of audio data! (seconds: {perf_counter()})")

with VoluxAudioStream(
    on_data=on_data,
    chunk_size=CHUNK_SIZE,
    channels=CHANNEL_COUNT
) as audio_stream:
    # keep stream open until script closed
    while True:
        sleep(1)
```

#### Buffered Example

This Python code continuously prints the current buffer of audio data being read from an audio stream at a specified rate.

```python
from voluxaudio import VoluxAudioStream
from time import sleep

CHUNK_SIZE=1024
CHANNEL_COUNT=2
BUFFER_SIZE_IN_SECONDS = 1
BUFFER_READS_PER_SECOND = 60

with VoluxAudioStream(
    chunk_size=CHUNK_SIZE,
    channels=CHANNEL_COUNT,
    buffer_size_in_seconds=BUFFER_SIZE_IN_SECONDS
) as audio_stream:
    while True:
        print(f"buffer: {audio_stream.buffer}")
        sleep(1/BUFFER_READS_PER_SECOND)
```

#### Audio-visualization Example

This Python code opens an audio stream using the `voluxaudio` library with buffering enabled. It defines a function `on_data()` that does nothing and is called every time new samples are gathered. Within the `while` loop, it calculates the weakly approximated amplitude of the audio stream by taking the last 2048 samples of the left and right channels and averaging their absolute values. It then prints a bar representing the amplitude by printing a number followed by a horizontal bar, where the length of the bar is proportional to the amplitude. The script waits for approximately 50 milliseconds before repeating the loop.

This audio stream comes from your system's default recording device, which could either be a microphone or your computer/desktop audio.

![Voluxaudio Amplitude Example](assets/voluxaudio-amplitude-example.gif)

```python
from voluxaudio import VoluxAudioStream
import numpy as np
from time import sleep

# call this every time new samples gathered
def on_data(*args, **kwargs):
    return

# open an audio stream with buffering enabled
with VoluxAudioStream(
    on_data=on_data,
    chunk_size=2048,
    channels=2,
    buffer_size_in_seconds=2,
) as audio_stream:

    # repeat until script stopped
    while True:

        # weakly approximate amplitude
        samples = audio_stream.buffer
        sample_count = len(samples)
        samples_per_channel = np.swapaxes(samples, 0, 1)
        L_channel_e = np.average(np.abs(samples_per_channel[0][-2048:])) / sample_count
        R_channel_e = np.average(np.abs(samples_per_channel[1][-2048:])) / sample_count
        e = (L_channel_e + R_channel_e) / 2

        # print bar
        print(f"{e:<3.3f} " + int(e*100) * '|')

        # wait ~50ms
        sleep(1 / 20)
```

- This is a simple example, but more complex audio processing is possible.
- A bar is printed every 50ms, changing length based on the approximated amplitude.
- The system volume may affect results, to test this dramatically increase/decrease your system volume to see if the bar length is affected. This applies to computer/desktop audio, not microphones.
- Buffering is used as `buffer_size_in_seconds` is specified.

## Todo List

- [x] Get simple `VoluxAudioStream` class working
- [x] Make `VoluxAudioStream` class highly configurable
- [x] Add basic example to documentation
- [x] Add basic documentation
- [x] Add more examples to documentation
- [x] Add links
- [ ] Add more detailed documentation

## Links

<!-- TODO: add website link -->
- 📖 &nbsp;[Documentation](https://gitlab.com/volux/voluxaudio)
- 🐍 &nbsp;[Latest Release](https://pypi.org/project/voluxaudio)
- 🧰 &nbsp;[Source Code](https://gitlab.com/volux/voluxaudio)
- 🐞 &nbsp;[Issue Tracker](https://gitlab.com/volux/voluxaudio/-/issues)
- `🐦 Twitter` &nbsp;[@DrTexx](https://twitter.com/DrTexx)
- `📨 Email` &nbsp;[denver.opensource@tutanota.com](mailto:denver.opensource@tutanota.com)
