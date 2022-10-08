export default function createInt8TypedArray(length, position, value) {
    try {
      const bf = new ArrayBuffer(length);
      const int8 = new DataView(bf);
      int8.setInt8(position, value);
      return int8;
    } catch (err) {
      throw Error('Position outside range');
    }
  }
