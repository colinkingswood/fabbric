import React from 'react';
import { render, waitFor, fireEvent } from '@testing-library/react';
import axios from 'axios';

import App from './App';

jest.mock('axios');

describe('Item rendering and selection', () => {
  it('renders items and allows selection', async () => {
    const mockItems = [
      {"id":1,"name":"Item1","thumbnail":"http://localhost:8000/media/cache/a8/03/a803b6e5f8092f48807356a93ea387bf.png","color":"white","description":null},
      {"id":2,"name":"Item2","thumbnail":"http://localhost:8000/media/cache/24/08/2408be3a968c4ba6345145a9022b92e4.png","color":"white","description":null},
      {"id":3,"name":"Item3","thumbnail":"http://localhost:8000/media/cache/7d/a8/7da892091c2e40d674fa6784daeca44b.png","color":"white","description":null}
    ];

    axios.get.mockResolvedValue({ data: mockItems });
    const { getByText, getAllByRole, getByLabelText, getByAltText} = render(<App />);

    await waitFor(() => {
      expect(getByText('Item1')).toBeInTheDocument();
    });

    // Now that items are loaded, continue with the rest of the test
    mockItems.forEach(item => {
      expect(getByText(item.name)).toBeInTheDocument();
    });


    const listItemElements = getAllByRole('listitem');
    expect(listItemElements.length).toBe(mockItems.length);

    // Click the first item
    fireEvent.click(listItemElements[0]);

    // check that the Choose a color appears
    await waitFor(() => {
      expect(getByText('Choose a custom color')).toBeInTheDocument();
    });

    const colorPicker = getByLabelText('Choose a custom color');

    // small image from https://gist.github.com/ondrek/7413434
    const mockCustomImage =  'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==';
    axios.post.mockResolvedValue({ data: mockCustomImage });

    // select a color
    fireEvent.change(colorPicker, { target: { value: '#ff0000' } });

    // check if the image source has changed after the POST request
    await waitFor(() => {
      const updatedImage = getByAltText('Item1'); // Assuming 'alt' attribute is set to the item's name
      expect(updatedImage.src).toBe(mockCustomImage);
    });


  });
});