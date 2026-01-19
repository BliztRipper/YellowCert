/**
 * API Service for YellowCert Backend
 */

import axios from 'axios';

// Use environment variable for production, fallback to localhost for development
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

/**
 * Upload image for certificate detection
 * @param {File} file - Image file to analyze
 * @returns {Promise} API response with detections
 */
export const detectCertificate = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post(`${API_URL}/predict`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw new Error(
      error.response?.data?.error ||
      'Failed to connect to server. Please try again.'
    );
  }
};

/**
 * Check API health status
 * @returns {Promise} API health status
 */
export const checkHealth = async () => {
  try {
    const response = await axios.get(`${API_URL}/`);
    return response.data;
  } catch (error) {
    throw new Error('Failed to connect to API');
  }
};
