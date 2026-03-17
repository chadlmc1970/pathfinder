import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Production API URL - NO localhost
const API_BASE_URL = 'https://pathfinder-api.onrender.com';

// API Client instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Types matching backend schemas
export interface Career {
  id: number;
  title: string;
  industry_sector: string;
  description: string;
  salary_range_min: number | null;
  salary_range_max: number | null;
  education_required: string;
  skills: string[] | null;
  pathway: any | null;
  created_at: string;
  updated_at: string;
}

export interface Video {
  id: number;
  career_id: number;
  blob_url: string;
  thumbnail_url: string | null;
  duration_seconds: number;
  transcript: string | null;
}

export interface VideoWithCareer extends Video {
  career: Career;
}

export interface EngagementEvent {
  user_id: number;
  career_id: number;
  video_id: number;
  action: 'watched' | 'liked' | 'saved' | 'skipped' | 'shared';
  watch_duration_seconds?: number;
}

export interface Recommendation {
  id: number;
  user_id: number;
  career_id: number;
  score: number;
  reason: string;
  created_at: string;
  career?: Career;
}

// User management
export const getUserId = async (): Promise<number> => {
  try {
    const userId = await AsyncStorage.getItem('user_id');
    if (userId) {
      return parseInt(userId, 10);
    }
    // Create a temporary user ID for demo purposes
    // In production, this would come from proper authentication
    const newUserId = Math.floor(Math.random() * 10000) + 1;
    await AsyncStorage.setItem('user_id', newUserId.toString());
    return newUserId;
  } catch (error) {
    console.error('Error getting user ID:', error);
    return 1; // Fallback user ID
  }
};

// API Functions

/**
 * Get all careers
 */
export const getCareers = async (): Promise<Career[]> => {
  try {
    const response = await apiClient.get<Career[]>('/api/v1/careers/');
    return response.data;
  } catch (error) {
    console.error('Error fetching careers:', error);
    throw error;
  }
};

/**
 * Get single career by ID
 */
export const getCareer = async (id: number): Promise<Career> => {
  try {
    const response = await apiClient.get<Career>(`/api/v1/careers/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching career ${id}:`, error);
    throw error;
  }
};

/**
 * Get all videos or videos for a specific career
 */
export const getVideos = async (careerId?: number): Promise<Video[]> => {
  try {
    const url = careerId
      ? `/api/v1/videos/?career_id=${careerId}`
      : '/api/v1/videos/';
    const response = await apiClient.get<Video[]>(url);
    return response.data;
  } catch (error) {
    console.error('Error fetching videos:', error);
    throw error;
  }
};

/**
 * Get videos with career data enriched
 */
export const getVideosWithCareers = async (): Promise<VideoWithCareer[]> => {
  try {
    const [videos, careers] = await Promise.all([
      getVideos(),
      getCareers(),
    ]);

    // Map careers by ID for quick lookup
    const careerMap = new Map(careers.map(c => [c.id, c]));

    // Enrich videos with career data
    return videos
      .map(video => ({
        ...video,
        career: careerMap.get(video.career_id)!,
      }))
      .filter(v => v.career); // Filter out videos without careers
  } catch (error) {
    console.error('Error fetching videos with careers:', error);
    throw error;
  }
};

/**
 * Record engagement event (like, save, skip, etc.)
 */
export const recordEngagement = async (
  event: Omit<EngagementEvent, 'user_id'>
): Promise<void> => {
  try {
    const userId = await getUserId();
    await apiClient.post('/api/v1/engagement/', {
      user_id: userId,
      ...event,
    });
  } catch (error) {
    console.error('Error recording engagement:', error);
    // Don't throw - engagement tracking failures shouldn't break UX
  }
};

/**
 * Get AI-powered career recommendations for current user
 */
export const getRecommendations = async (
  limit: number = 5
): Promise<Recommendation[]> => {
  try {
    const userId = await getUserId();
    const response = await apiClient.get<Recommendation[]>(
      `/api/v1/recommendations/?user_id=${userId}&limit=${limit}`
    );
    return response.data;
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    throw error;
  }
};

/**
 * Health check
 */
export const checkHealth = async (): Promise<boolean> => {
  try {
    const response = await apiClient.get('/health');
    return response.status === 200;
  } catch (error) {
    console.error('API health check failed:', error);
    return false;
  }
};

export default apiClient;
