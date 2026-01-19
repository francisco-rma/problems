Once a max heap is established on top of an array A, it is relatively easy to sort it.
It is important that the limit of the heap be mutable and that the heap construction take that into account and ignore items that lie beyond the established limit. 

The root element of the array is guaranteed to be the largest element, so putting it into it's final position means simply swapping it with the element at the index of the heap limit L:

`heap[0], heap[L] = heap[L], heap[0]`

Then the heap limit must be decremented by 1 to ignore items that are already in their place:

`L = L - 1`

Now the heap may be invalid, so we need to reconstruct it:

`max_heapify(A,0)`

where max_heapify is the heap construction procedure.